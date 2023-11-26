import socket

def start_client(host, port, request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send a SPARQL query to the server
    client_socket.sendall(f"SPARQL:{request}".encode())
    print(f"Sent SPARQL query to server: {request}")

    # Receive the server's response
    response = client_socket.recv(1024)
    print(f"Received response from server:\n{response.decode()}")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    server_host = '127.0.0.1'  # localhost
    server_port = 12345

    # SPARQL query to request information from the knowledge base
    sparql_query = """
        
        SELECT ?label ?threshold
        WHERE {
            ind:kpi3 rdfs:label ?label .
            ind:kpi3 prop:hasMin ?threshold .
        }
    """

    start_client(server_host, server_port, sparql_query)
