using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Linq;

namespace Panginated_API
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Task.Run(() => Main1()).Wait();
           // Console.ReadLine();
        }
        static async void Main1()
        {
            Console.WriteLine("Hello, World!");
            var page = 1;
            var perPage = 5;
            var accessToken = "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";

            HttpClient client = new HttpClient();
            client.DefaultRequestHeaders.UserAgent.Add(new System.Net.Http.Headers.ProductInfoHeaderValue("AppName", "1.0"));
            client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));
            client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Token", accessToken);
            while (true)
            {
                try
                {
                    var response = client.GetAsync($"https://api.github.com/users/ahsan7162/repos?page={page}&per_page={perPage}").Result;
                    if (!response.IsSuccessStatusCode)
                        break;
                    var data = await response.Content.ReadAsStringAsync();
                    JArray? obj = JsonConvert.DeserializeObject(data) as JArray;
                    if (obj is not null && obj.Count == 0)
                        break;
                    Console.WriteLine(obj);
                    page++;
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                }
            }
            Console.ReadLine();
        }
    }
}
