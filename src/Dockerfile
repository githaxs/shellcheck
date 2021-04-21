FROM koalaman/shellcheck:stable as binary

FROM public.ecr.aws/lambda/python:3.8 as deps
COPY --from=binary /bin/shellcheck /bin/

RUN yum install -y git

COPY requirements.txt .
RUN python3.8 -m pip install -r requirements.txt

COPY . .

# Command can be overwritten by providing a different command in the template directly.
CMD ["handler.lambda_handler"]
