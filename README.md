## Infilect Backend Engineering Assignment

### Description
 Following is my solution to Infilect's chess player problem.
 The problem statement is in the `/problem-statement` directory, kindly
refer to that for more information.
 
As mentioned in the problem statement, I have created a local server and exposed
`/chess/<slug>` endpoint, where a user can provide all the positions in post body,
and target user in the `slug` path parameter.
```
{
    "positions":{"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}
}

http://localhost:8000/chess/rook
```

The response of the above code would be all the valid positions for our rook, e.g.
```
{
    "valid_moves": [
        "A5",
        "H1",
        "H3",
        "H4",
        "H8"
    ]
}
```


### Project setup and steps to run

The project is dockerize using a `Dockerfile`.
Following are the steps to run the application on `Docker`.

- Build this application into a python:3.9 docker image using
```
docker build -t ${custom_image_name} .
```

- Now that we have our image build we could just run it
on current shell or run the image in background/detach mode using:

```
Run on current shell:
docker run -p 8000:8000 ${custom_image_name}

Run on detach mode:
docker run -d -p 8000:8000 ${custom_image_name}
```