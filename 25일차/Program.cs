using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Timers;
using Microsoft.Azure.Devices.Client;
using Newtonsoft;
using IoTenv;

namespace IoTClient
{
    internal class Program
    {
        private static System.Timers.Timer SensorTimer;
        private const string DeviceConnectionString = IoTenv.DeviceConnectionString;
        private const string DeviceID = "Device1";
        private static DeviceClient SensorDevice = null;

        private static DummySensor DummySensor = new DummySensor();
        static void Main(string[] args)
        {
            SetTimer();

            SensorDevice = DeviceClient.CreateFromConnectionString(DeviceConnectionString, DeviceID);

            if(SensorDevice == null)
            {
                Console.WriteLine("Failed to create DeviceClient!");
                SensorTimer.Stop();
                // 혹시 클라이언트가 만들어지지 않았다면, 타이머를 정지한다
            }

            Console.WriteLine("\nPress Enter key to exit the application...\n");
            Console.WriteLine("The application started at {0:HH.mm.ss.fff}", DateTime.Now);
            Console.ReadLine();
            // 사용자의 입력을 대기하며 계속 신호를 보낸다
            SensorTimer.Stop();
            SensorTimer.Dispose();
        }

        private static void SetTimer()
        {
            SensorTimer = new System.Timers.Timer(2000);
            // 2초(2000ms)마다 이벤트 발생시킴 -> 2초마다 elapsed가 특정 동작을 해줌
            SensorTimer.Elapsed += SensorTimer_Elapsed;
            SensorTimer.AutoReset = true;
            SensorTimer.Enabled = true;
        }

        private static void SensorTimer_Elapsed(object sender, ElapsedEventArgs e)
        {
            Console.WriteLine("The Elapsed event was raised at {0:HH:mm:ss:fff}", e.SignalTime);
            // e.Signaltime 객체에 위에서 이벤트가 발생할 때의 시간이 기록됨
            SendEvent();
        }

        private static async void SendEvent()
        {
            WeatherModel model = DummySensor.GetWeatherModel(DeviceID);

            string json = Newtonsoft.Json.JsonConvert.SerializeObject(model);

            Console.WriteLine(json);
        }
    }
}
