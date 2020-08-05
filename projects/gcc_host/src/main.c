#include <stdlib.h>
#include <stdio.h>
//#include "gpio_if.h"

#ifdef WINNT
#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>
#else
#include <sys/socket.h>
#endif

int main(void)
{
    WSADATA wsaData;
    SOCKET sc;
    struct addrinfo *result = NULL,
                    hints;
    const char *sendbuf = "this is a test";
    int iResult;
    iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
    if (iResult != 0)
    {
        printf("WSAStartup failed with error: %d\n", iResult);
        return 1;
    }

    ZeroMemory( &hints, sizeof(hints) );
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;

    // Resolve the server address and port
    iResult = getaddrinfo("localhost", "9999", &hints, &result);
    if ( iResult != 0 ) {
        printf("getaddrinfo failed with error: %d\n", iResult);
        WSACleanup();
        return 1;
    }

    sc = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
    iResult = connect(sc, result->ai_addr, result->ai_addrlen);
    iResult = send( sc, sendbuf, (int)strlen(sendbuf), 0 );
    iResult = shutdown(sc, SD_SEND);
    closesocket(sc);
    WSACleanup();
    setvbuf(stdout, NULL, _IONBF, 0);
    //gpio_init();
    printf("End Of Main\n");
    return 0;
}
