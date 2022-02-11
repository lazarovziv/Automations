FROM python:3
ADD login.py /
RUN pip install selenium
CMD ["python", "./login.py"]
