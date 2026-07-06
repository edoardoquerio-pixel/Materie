using Microsoft.Data.SqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Text;

namespace StudentiGUI
{
    internal class StudentiDAL
    {
        private SqlConnectionStringBuilder connectionString;

        //connessione al database
        public StudentiDAL()
        {
            connectionString = new SqlConnectionStringBuilder();
            connectionString.DataSource = "localhost";
            connectionString.UserID = "cloud";
            connectionString.Password = "Its-2026";
            connectionString.InitialCatalog = "Anagrafica";
            connectionString.TrustServerCertificate = true;
        }

        //lettura tutti i dati
        public List<Studente> Elenco()
        {
            var elenco = new List<Studente>();

            using (SqlConnection connection = new SqlConnection())
            {
                connection.ConnectionString= connectionString.ConnectionString;
                connection.Open();

                using (SqlCommand command = new SqlCommand())
                { 
                    command.CommandText = "SELECT * FROM Studente";
                    command.CommandType = CommandType.Text;
                    command.Connection = connection;

                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            elenco.Add(new Studente { Matricola=reader.GetInt32("Matricola")
                                , Nome=reader.GetString("Nome")
                                , Cognome=reader.GetString("Cognome")
                                , Email=reader.GetString("Email")
                                , Classe=reader.GetString("Classe") });
                        }
                    }
                }
            }
            return elenco;
        }

        //lettura di uno specifico studente di cui conosco la matricola
        public Studente Dettaglio(int matricola)
        {
            Studente? studente = null;

            using (SqlConnection connection = new SqlConnection())
            {
                connection.ConnectionString = connectionString.ConnectionString;
                connection.Open();

                using (SqlCommand command = new SqlCommand())
                {
                    command.CommandText = $"SELECT * FROM Studente where matricola=@Matricola";
                    command.CommandType = CommandType.Text;
                    command.Connection = connection;
                    command.Parameters.Add("@matricola", SqlDbType.Int).Value = matricola;

                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            studente = new Studente
                            {
                                Matricola = reader.GetInt32("Matricola"),
                                
                                Nome = reader.GetString("Nome"),
                                
                                Cognome = reader.GetString("Cognome"),
                                
                                Email = reader.GetString("Email"),
                                Classe = reader.GetString("Classe")
                            };
                        }
                    }
                }
            }
            return studente;
        }

        //inserimento di un nuovo studente
        //public bool Nuovo(Studente studente) {

        //    int rows = 0;
        //    using (SqlConnection connection = new SqlConnection())
        //    {
        //        connection.ConnectionString = connectionString.ConnectionString;
        //        connection.Open();

        //        using (SqlCommand command = new SqlCommand())
        //        {
        //            command.CommandText = $"INSERT INTO Studente(Matricola, Nome, Cognome, Email, Classe) VALUES ({studente.Matricola},'{studente.Nome}','{studente.Cognome}','{studente.Email}','{studente.Classe}')";
        //            command.CommandType = CommandType.Text;
        //            command.Connection = connection;

        //            rows = command.ExecuteNonQuery(); //per mandare in esecuzione INSERT, UPDATE, DELETE

        //            }
        //        }
        //    return rows == 1;
        //    }

        public void Nuovo(Studente studente)
        {

           
            using (SqlConnection connection = new SqlConnection())
            {
                connection.ConnectionString = connectionString.ConnectionString;
                connection.Open();

                using (SqlCommand command = new SqlCommand())
                {
                    command.CommandText = $"INSERT INTO Studente(Matricola, Nome, Cognome, Email, Classe) VALUES (@Matricola,@Nome, @Cognome, @Email, @Classe)";
                    command.CommandType = CommandType.Text;
                    command.Connection = connection;

                    // parametrizzazione - eviate errori su SQL SERVER e SQL INJECTION
                    command.Parameters.Add("@Matricola",SqlDbType.Int).Value = studente.Matricola;
                    command.Parameters.Add("@Nome",SqlDbType.VarChar,50).Value = studente.Nome;
                    command.Parameters.Add("@Cognome",SqlDbType.VarChar,50).Value = studente.Cognome;
                    command.Parameters.Add("@Email",SqlDbType.VarChar,50).Value = studente.Email;
                    command.Parameters.Add("@Classe",SqlDbType.VarChar,50).Value = studente.Classe;

                    command.CreateParameter();

                    int rows = command.ExecuteNonQuery(); //per mandare in esecuzione INSERT, UPDATE, DELETE

                    if (rows != 1)
                    {
                        throw new Exception("inserimento studente fallito");
                    }

                }
            }
        }



        //modifica di uno studente esistente
        public void Modifica(Studente studente)
        {


            using (SqlConnection connection = new SqlConnection())
            {
                connection.ConnectionString = connectionString.ConnectionString;
                connection.Open();

                using (SqlCommand command = new SqlCommand())
                {
                    command.CommandText = $"UPDATE Studente SET Nome = @Nome, Cognome = @Cognome, Email = @Email, Classe = @Classe WHERE Matricola = @Matricola";
                    command.CommandType = CommandType.Text;
                    command.Connection = connection;

                    // parametrizzazione - eviate errori su SQL SERVER e SQL INJECTION
                    command.Parameters.Add("@Matricola", SqlDbType.Int).Value = studente.Matricola;
                    command.Parameters.Add("@Nome", SqlDbType.VarChar, 50).Value = studente.Nome;
                    command.Parameters.Add("@Cognome", SqlDbType.VarChar, 50).Value = studente.Cognome;
                    command.Parameters.Add("@Email", SqlDbType.VarChar, 50).Value = studente.Email;
                    command.Parameters.Add("@Classe", SqlDbType.VarChar, 50).Value = studente.Classe;

                    command.CreateParameter();

                    int rows = command.ExecuteNonQuery(); //per mandare in esecuzione INSERT, UPDATE, DELETE

                    if (rows != 1)
                    {
                        throw new Exception("Modificia studente fallita");
                    }

                }
            }
        }


        //eliminazione di uno studente

        public void Elimina(Studente studente)
        {


            using (SqlConnection connection = new SqlConnection())
            {
                connection.ConnectionString = connectionString.ConnectionString;
                connection.Open();

                using (SqlCommand command = new SqlCommand())
                {
                    command.CommandText = $"DELETE FROM Studente WHERE Matricola = @Matricola";
                    command.CommandType = CommandType.Text;
                    command.Connection = connection;

                    // parametrizzazione - eviate errori su SQL SERVER e SQL INJECTION
                    command.Parameters.Add("@Matricola", SqlDbType.Int).Value = studente.Matricola;

                    command.CreateParameter();

                    int rows = command.ExecuteNonQuery(); //per mandare in esecuzione INSERT, UPDATE, DELETE

                    if (rows != 1)
                    {
                        throw new Exception("Eliminazione studente fallita");
                    }

                }
            }
        }
    }
}
