# FASTTEXT language classifier

## Usage

The docker image can be built using the following command:

```
docker build -t languagedetection .
```

After building the image you can run it using following command. The -d flag makes it run in detached mode and the --rm flag will remove the docker container after it has been shut down.

```
docker run --rm -d --name $name -p 5000:5000 languagedetection
```

Using the command above maps port 5000 in the container to port 5000 on your host system.