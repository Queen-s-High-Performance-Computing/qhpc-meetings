FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libc6-dev openmpi-bin libopenmpi-dev openssh-server openssh-client \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --uid 1000 --create-home --shell /bin/bash mpiuser \
    && passwd -d mpiuser \
    && mkdir -p /run/sshd

COPY mpi_hello.c /tmp/mpi_hello.c
RUN mpicc -std=c11 -Wall -Wextra -Werror -O2 /tmp/mpi_hello.c \
    -o /home/mpiuser/mpi_hello && rm /tmp/mpi_hello.c
COPY ssh_config /etc/ssh/ssh_config.d/99-qhpc.conf
COPY --chown=mpiuser:mpiuser sshd_config /home/mpiuser/.sshd_config

USER 1000:1000
WORKDIR /home/mpiuser
EXPOSE 2222
CMD ["/usr/sbin/sshd", "-De", "-f", "/home/mpiuser/.sshd_config"]
