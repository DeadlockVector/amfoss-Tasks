using System;
using System.Text;

// added these
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Newtonsoft.Json;

using System.Net;
using System.Net.Mail;
using System.Net.Security;
using System.Net.Sockets;


// check whether all required namespaces are imported   (Done hopefully? recheck)
public class SynchronousSocketListener
{

    // Incoming data from the client. 
    public static string data = null;

    public static void StartListening()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new Byte[1024];

        // Establish the local endpoint for the socket.   (Added from website)   dont think we need to add line 23??
        //IPEndPOINT ep = new IPendPoint(IPAddress.Loopback, 1234);     // so many semicolons  

        // Dns.GetHostName returns the name of the
        // host running the application.  
         
        IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
        IPAddress ipAddress = ipHostInfo.AddressList[0];
        IPEndPoint localEndPoint = new IPEndPoint(ipAddress, 8080);

        // Check whether TCP Socket is created correctly

        //Socket listener = new Socket(ipAddress.AddressFamily);       //wrong way probably, corrected line 41
        Socket listener = new(
            ipAddress.AddressFamily,
            SocketType.Stream,
            ProtocolType.Tcp);

        //var handler = listener.AcceptAsync();      //Defining variable handler here   (todo of line 55, 56) is this even needed?? doesn't seem like it
                                                                                           // already defined line 63??
        // Bind the socket to the local endpoint and
        // listen for incoming connections.  
        string fileName = "file.json";
        
        try
        {
            listener.Bind(localEndPoint);
            listener.Listen(10);

            // Start listening for connections.
            
            while (true)
            {
                Console.WriteLine("Waiting for a connection...");
                // Program is suspended while waiting for an incoming connection.  
                Socket handler = listener.Accept();
                string? data = null;
                bytes = new byte[1024];

                // An incoming connection needs to be processed.  
                // check if the varibale is defined or not also even correctly defined
                int bytesRec = handler.Receive(bytes);
                data = Encoding.ASCII.GetString(bytes, 0, bytesRec);         //var data returns error 

                Console.WriteLine("Text received : {0}", data);
                //string[] dataArr = new String[3];                  //CHECK HOW TO SPLIT
                string[] dataArr = data.Split(",");
                string name = dataArr[0];
                string intrests = dataArr[1];
                string mail = dataArr[2];
                string jsonData = "{ \"name\": \"" + name + "\", \"intrests\": \"" + intrests + "\", \"mail\": \"" + mail + "\" }";
                Console.WriteLine("Name: {0}", name);
                Console.WriteLine("Intrests: {0}", intrests);
                Console.WriteLine("Email:{0}", mail);

                string path=@"/home/isocyanate/FindTheBug/task-05/Server/bin/Debug/net6.0";          //checking if file exists or not     
                if (File.Exists(path))                   // if condition also added from sample  - changed response to data in syntax
                {
                    using (StreamWriter sw = File.AppendText(fileName))
                    {
                        sw.WriteLine(jsonData);
                    }
                }
                else
                {
                    using (StreamWriter sw = File.CreateText(fileName))
                    {
                        sw.WriteLine(jsonData);
                    }
                }
                handler.Shutdown(SocketShutdown.Both);
                handler.Close();
            }

        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }

        Console.WriteLine("\nPress ENTER to continue...");
        Console.Read();

    }
    // check the main function
    public static int Main(String[] args)    //Potential bug >> convert String to string (nevermind lol)
    {
        StartListening();    //no error when Start() commented out
        return 0;
    }
}