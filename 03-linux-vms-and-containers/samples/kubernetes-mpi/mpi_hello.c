#include <mpi.h>
#include <stdio.h>

int main(int argc, char **argv) {
    int rank, size, hostname_length;
    char hostname[MPI_MAX_PROCESSOR_NAME];
    long long local, total = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Get_processor_name(hostname, &hostname_length);

    printf("Rank %d of %d on %.*s\n", rank, size, hostname_length, hostname);
    fflush(stdout);
    local = (long long)rank + 1;
    MPI_Reduce(&local, &total, 1, MPI_LONG_LONG_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    long long expected = (long long)size * (size + 1LL) / 2;
    if (rank == 0) {
        printf("Sum of rank contributions: %lld (expected %lld)\n", total, expected);
    }
    MPI_Finalize();
    return rank == 0 && total != expected ? 1 : 0;
}
