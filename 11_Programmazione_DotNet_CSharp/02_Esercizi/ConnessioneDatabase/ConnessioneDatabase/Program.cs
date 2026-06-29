using Microsoft.Data.SqlClient;
using System.Data;

namespace ConnessioneDatabase
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Connessione al database SQL Server!");

            //accesso al dbms
            //preparazione della stringa di connessione
            //pacchetto di classi: ADO.NET

            SqlConnectionStringBuilder connectionString = new SqlConnectionStringBuilder();
            connectionString.DataSource = @"localhost";
            connectionString.UserID = "cloud";
            connectionString.Password = "Its-2026";
            connectionString.InitialCatalog = "Istat";
            connectionString.TrustServerCertificate = true;

            //accesso al database
            SqlConnection connection = new SqlConnection();
            connection.ConnectionString=connectionString.ConnectionString;
            connection.Open();
            Console.WriteLine("Connessione al DBMS Sql Server avvenuta con successo");

            //query al database
            string sql = "Select * from Regione";

            SqlCommand command = new SqlCommand();
            command.CommandText = sql;
            command.CommandType=CommandType.Text;
            command.Connection=connection;
            Console.WriteLine("Accesso al database avvenuto con successo");

            //estrazione dati da tabella temporanea
            SqlDataReader reader = command.ExecuteReader();

            Console.WriteLine("Elenco Regioni");
            Console.WriteLine($"Id, Denominazione, IdRipartizione");
            while (reader.Read())
            {
                Console.WriteLine($"{reader.GetInt32("Id")}, {reader.GetString("Denominazione")}, {reader.GetInt32("IdRipartizione")}");
            }

            //termina connessione
            reader.Close();
            command.Dispose();
            connection.Close();





        }
    }
}
