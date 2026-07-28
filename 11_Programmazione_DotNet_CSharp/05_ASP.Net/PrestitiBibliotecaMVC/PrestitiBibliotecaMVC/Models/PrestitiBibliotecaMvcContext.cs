using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace PrestitiBibliotecaMVC.Models;

public partial class PrestitiBibliotecaMvcContext : DbContext
{
    public PrestitiBibliotecaMvcContext()
    {
    }

    public PrestitiBibliotecaMvcContext(DbContextOptions<PrestitiBibliotecaMvcContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Libro> Libri { get; set; }

    public virtual DbSet<Prestito> Prestiti { get; set; }

    public virtual DbSet<Studente> Studenti { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see https://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseSqlServer("Server=localhost;Database=PrestitiBibliotecaMVC;Trusted_Connection=True;TrustServerCertificate=True");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Libro>(entity =>
        {
            entity.ToTable("Libro");

            entity.Property(e => e.Id).ValueGeneratedNever();
            entity.Property(e => e.Anno).HasMaxLength(50);
            entity.Property(e => e.Autore).HasMaxLength(50);
            entity.Property(e => e.Classificazione).HasMaxLength(50);
            entity.Property(e => e.Collocazione).HasMaxLength(50);
            entity.Property(e => e.Editore).HasMaxLength(50);
            entity.Property(e => e.Luogo).HasMaxLength(50);
            entity.Property(e => e.Titolo).HasMaxLength(50);
        });

        modelBuilder.Entity<Prestito>(entity =>
        {
            entity.ToTable("Prestito");

            entity.Property(e => e.DataPrestito).HasColumnType("datetime");
            entity.Property(e => e.DataRestituzione).HasColumnType("datetime");

            entity.HasOne(d => d.IdLibroNavigation).WithMany(p => p.Prestiti)
                .HasForeignKey(d => d.IdLibro)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_Prestito_Libro1");

            entity.HasOne(d => d.MatricolaNavigation).WithMany(p => p.Prestiti)
                .HasForeignKey(d => d.Matricola)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_Prestito_Studente1");
        });

        modelBuilder.Entity<Studente>(entity =>
        {
            entity.ToTable("Studente");

            entity.Property(e => e.Id).ValueGeneratedNever();
            entity.Property(e => e.Classe).HasMaxLength(50);
            entity.Property(e => e.Cognome).HasMaxLength(50);
            entity.Property(e => e.Email).HasMaxLength(50);
            entity.Property(e => e.Nome).HasMaxLength(50);
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
