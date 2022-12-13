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

// check whether all required namespaces are imported

public class SynchronousSocketClient
{

    public static void StartClient()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];

        // Connect to a remote device.  
        try
        {
            // Establish the remote endpoint for the socket.  
            // check if the port is defined or not
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
            IPAddress ipAddress = ipHostInfo.AddressList[0];
            IPEndPoint remoteEP = new IPEndPoint(ipAddress, 8080);

            // Check whether TCP Socket is created correctly
            // Socket sender = new Socket(ipAddress.AddressFamily);
            Socket sender = new(
                remoteEP.AddressFamily,                 //changed ipEndPoint.AddressFamily to remoteEP.AddressFamily >> Semms to work
                SocketType.Stream,
                ProtocolType.Tcp);

            //Socket client = new(
              //  remoteEP.AddressFamily,
                //SocketType.Stream,           //if I realized socket client and sender was the same thing I would have finished 5 days earlier
                //ProtocolType.Tcp);

            sender.ConnectAsync(remoteEP);      //changed ipEndPoint to remoteEP   >> seems to work
                                                      // await keeps giving error, so remove and see result
                                                    // changed await client.ConnectAsync(remoteEP); to client.ConnectAsync(remoteEP);
                                                    //seems to work

            // Connect the socket to the remote endpoint. Catch any errors.  
            try
            {
                sender.Connect(remoteEP);

                Console.WriteLine("Socket connected to {0}",
                    sender.RemoteEndPoint.ToString());

                // check if the variable is defined correctly or not
                Console.WriteLine("Enter the Person Name: ");
                var name = Console.ReadLine();                       // added var 
                Console.WriteLine("Enter the Person Intrest: ");
                var intrests = Console.ReadLine();                     // was int before
                Console.WriteLine("Enter the Person Email: ");
                var mail = Console.ReadLine();                        // added var here as well
                // Encode the data string into a byte array.  
                // check the data type of the data you are sending.
                byte[] msg = Encoding.ASCII.GetBytes(name + "," + intrests + "," + mail);

                // Send the data through the socket.  
                int bytesSent = sender.Send(msg);

                // Close the socket.
                sender.Close();
            }
            catch (ArgumentNullException ane)
            {
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se)
            {
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }

        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
    }

    // check the main function
    public static int Main(String[] args)
    {
        StartClient();
        return 0;
    }
}
