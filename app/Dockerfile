FROM ubuntu as builder
COPY ./app.py .
RUN apt-get update \
  && apt-get install python3 -y \
  && apt-get install python3-pip -y \
  && apt-get install patchelf binutils -y \
  && pip3 install pyinstaller staticx \
  && pyinstaller --onefile app.py \
  && staticx --strip dist/app dist/app-stat \
  && strip -s -R .comment -R .gnu.version --strip-unneeded dist/app-stat \
  && mkdir dist/tmp && rm -rf dist/app \
  && chmod -c 755 dist/app-stat && chown -c 0:0 dist/app-stat

FROM scratch
COPY --from=builder dist/ /
EXPOSE 8000
ENTRYPOINT ["./app-stat"]