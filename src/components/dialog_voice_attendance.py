import streamlit as st

from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase

import pandas as pd

from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime


@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):

    st.write(
        'Record audio of students saying I am present. '
        'Then AI will recognize the students'
    )

    # Step 1: Record classroom audio
    audio_data = st.audio_input("Record classroom audio")

    # Step 2: Analyze Audio Button
    if st.button('Analyze Audio', width='stretch', type='primary'):

        # Check audio
        if audio_data is None:
            st.warning("Please record classroom audio first.")
            return

        with st.spinner('Processing Audio data...'):

            # Step 3: Fetch enrolled students
            try:

                enrolled_res = supabase.table(
                    'subjects_students'
                ).select(
                    "*, students(*)"
                ).eq(
                    'subject_id', selected_subject_id
                ).execute()

                enrolled_students = enrolled_res.data

            except Exception as e:

                st.error("Failed to fetch enrolled students from Supabase.")

                st.exception(e)

                return

            # Step 4: Check enrolled students
            if not enrolled_students:
                st.warning('No students enrolled in this course.')
                return

            # Step 5: Get registered voice embeddings
            candidates_dict = {

                s['students']['student_id']:
                s['students']['voice_embedding']

                for s in enrolled_students

                if s.get('students')
                and s['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.error(
                    'No enrolled students have voice profiles registered.'
                )
                return

            # Step 6: Read audio bytes
            audio_bytes = audio_data.read()

            if not audio_bytes:
                st.error("Recorded audio is empty. Please record again.")
                return

            # Step 7: Process classroom audio
            try:

                detected_scores = process_bulk_audio(
                    audio_bytes,
                    candidates_dict
                )

            except Exception as e:

                st.error("Voice processing failed.")

                st.exception(e)

                return

            # Step 8: Generate attendance results
            results = []
            attendance_to_log = []

            current_timestamp = datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%S"
            )

            for node in enrolled_students:

                student = node['students']

                score = detected_scores.get(
                    student['student_id'], 0.0
                )

                is_present = bool(score > 0)

                results.append({

                    "Name": student['name'],

                    "ID": student['student_id'],

                    "Source": score if is_present else "-",

                    "Status": "✅ Present" if is_present else "❌ Absent"

                })

                attendance_to_log.append({

                    'student_id': student['student_id'],

                    'subject_id': selected_subject_id,

                    'timestamp': current_timestamp,

                    'is_present': bool(is_present)

                })

            # Step 9: Save results
            st.session_state.voice_attendance_results = (
                pd.DataFrame(results),
                attendance_to_log
            )

    # Step 10: Display attendance results
    if st.session_state.get('voice_attendance_results'):

        st.divider()

        df_results, logs = st.session_state.voice_attendance_results

        show_attendance_result(df_results, logs)