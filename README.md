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