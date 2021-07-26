# evaluation
Tp

A) avec dockerfile :

    in dockerfile folder exec :

        Docker build -t imageNmae .
        docker run -it imageName 

    type requested inputs


B) avec docker compose:

    in the same folder execute :

        docker-compose run eval bash
        docker run -it imageName 
    
    then check the "output.txt" on the same path file containign scan results (file created after launching the container)


