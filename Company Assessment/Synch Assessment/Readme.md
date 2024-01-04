# Sych Assessment

## PART_A
- Part_A.py contains a flask web application for synchronous /predict endpoint and the docker file for building the application.
- A flask server on port 8080 will start up after running the docker image.
- you have to add input in json format like {"input_data" : "Data"}.
- after proccessing the request it will return the response and this response is not stored in an any memory.

## PART_B
- Part_B.py contains a flask web application for asynchronous /predict endpoint and the docker file for building the application
- Similar to Part_A a web server starts listening on port 8080 but now the request it will be asynchronous.
- You have to set a flag "Async-Mode" in header to make request asynchronous if you don't do that it will behave in synchronous way.
- When you send a request to this endpoint it is added into queue
- There is backgroud worker that continuously monitor if anything is added into queue. If anything is added it will pick it out from the queue and then process it to make predictions.
- All requests are served in FIFO manner

### Bug
- I have use the basic queue structure provided by python to implement queue in the code a problem using that is that when I get item from queue for procession it removes that from queue and that process it so if anyone make request during the processing time he will see an error that id not found but it will doing processing on backend so this is samll bug in the code
