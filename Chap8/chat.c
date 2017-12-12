/*
=============================================================
Functionality adopted from: RUCHIR SHARMA (@ruchirsharma1993)
=============================================================
*/

#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <time.h>

void server(int port){
	int fd = 0;
	char buff[1024];
	char nbuff[1024];
	
	//Setup Buffer Array
	memset(buff, '0',sizeof(buff));	

	//Create Socket
	fd = socket(AF_INET, SOCK_STREAM, 0);
    	if(fd<0)
	{
		perror("Client Error: Socket not created succesfully");
		return;
	}

	//Structure to store details
	struct sockaddr_in server; 
	memset(&server, '0', sizeof(server)); 

	//Initialize	
	server.sin_family = AF_INET;
	server.sin_port = htons(port); 
        server.sin_addr.s_addr = htonl(INADDR_ANY);
   

	bind(fd, (struct sockaddr*)&server, sizeof(server)); 

	int in;
	
	listen(fd, 10); 
	while(	in = accept(fd, (struct sockaddr*)NULL, NULL))
	{		
		int childpid,n;
		if ( (childpid = fork ()) == 0 ) 
		{
		
			//printf ("\nOne Client Connected !! ");
		
			//close listening socket
			close (fd);
		
			//Clear Zeroes
			bzero(buff,256);
			bzero(nbuff,256);
							
			while ( (n = recv(in, buff, 256,0)) > 0)  
			{
			
				printf("Server Received: %s\n",buff);
				fflush(stdout);
                time_t curtime;
                time(&curtime);

                char *ts = ctime(&curtime);
                strcat(ts, buff);
				//Send the reversed input
				send(in, ts, strlen(ts), 0);
		
				bzero(buff,256);
										
			}
			close(in);
			exit(0);
		}
	}
}


void client(int port, char *ip)
{
	int fd = 0;
	char buff[1024];
	//Setup Buffer Array
	memset(buff, '0',sizeof(buff));	
	//Create Socket
	fd = socket(AF_INET, SOCK_STREAM, 0);
    	if(fd<0)
	{
		perror("Client Error: Socket not created succesfully");
		fflush(stderr);
		return;
	}
	//Structure to store details
	struct sockaddr_in server; 
	memset(&server, '0', sizeof(server)); 

	//Initialize	
	server.sin_family = AF_INET;
	server.sin_port =  htons(port);

	int in = inet_pton(AF_INET, ip, &server.sin_addr);
	if(in<0)
	{
		perror("Client Error: IP not initialized succesfully");
		fflush(stderr);
		return;
	}

	//Connect to given server	
	in = connect(fd, (struct sockaddr *)&server, sizeof(server));
	if(in<0)
	{
		perror("Client Error: Connection Failed.");
		fflush(stderr);
		return;
	}    	
	while(1)
	{
		printf("\nPlease enter the message: ");
		fflush(stdout);

    		bzero(buff,256);
    		fgets(buff,255,stdin);
			fflush(stdin);
    		
		    printf("\nSending to server: %s ",buff);
			fflush(stdout);
	
		/* Send message to the server */
    		in = send(fd,buff,strlen(buff),0);
		    if (in < 0) 
		    {
			 perror("\nClient Error: Writing to server");
			    fflush(stderr);
		    	return;
		    }
		    
		/* Now read server response */
		    bzero(buff,256);
		    in = recv(fd,buff,255,0);
		    if (in < 0) 
		    {
			 perror("\nClient Error: Reading from server");
			 fflush(stderr);
			 return;
		    }
		    printf("\nReceived FROM server:\n%s ",buff);
			fflush(stdout);
	}
	close(fd);
	return;
}

/*int main(){
	server(21567);
	return 0;
}*/


#include "Python.h"

static PyObject *chat_server(PyObject *self, PyObject *args){
	int port;
	if(!PyArg_ParseTuple(args, "i", &port))
	    return NULL;
	server(port);
	Py_RETURN_NONE;
}

static PyObject *chat_client(PyObject *self, PyObject *args){
    int port;
    char *ip;
    if(!PyArg_ParseTuple(args, "iS", &port, &ip))
        return NULL;
    client(port, ip);
    Py_RETURN_NONE;
}

static PyMethodDef chatMethods[] =
{
	{"client", chat_client, METH_VARARGS},
	{"server", chat_server, METH_VARARGS}
};

void initchat(){
	Py_InitModule("chat", chatMethods);
}