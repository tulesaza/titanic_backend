FROM python:3-onbuild

EXPOSE 9999

CMD ["python","./titanic.py"]