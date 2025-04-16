import imaplib
import email
from email.header import decode_header
import os
import docx
from PyPDF2 import PdfReader

def fetch_resumes(imap_server, email_id, password):
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_id, password)
        mail.select("inbox")

        status, messages = mail.search(None, '(HASATTACHMENT)')
        resume_files = []

        for num in messages[0].split():
            status, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else 'utf-8')
                    sender = msg.get("From")
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if "attachment" in content_disposition:
                                filename = part.get_filename()
                                if filename.endswith(('.pdf', '.docx')):
                                    file_data = part.get_payload(decode=True)
                                    resume_files.append({"filename": filename, "data": file_data})
        return resume_files
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []

def save_resume(resume_files, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for resume in resume_files:
        with open(os.path.join(save_dir, resume['filename']), 'wb') as f:
            f.write(resume['data'])