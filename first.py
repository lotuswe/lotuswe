print 'Hello World'


Server 端参数：
-s, --server，以 Server 模式运行；
-D, --daemon，在后台以守护进程运行；
-I, --pidfile file，指定 pid 文件；
-1, --one-off，只接受 1 次来自 Client 端的测试，然后退出。
Client 端参数
-c, --client ，以 Client 模式运行，并指定 Server 端的地址；
-u, --udp，以 UDP 协议进行测试；
-b, --bandwidth #[KMG][/#]，限制测试带宽。UDP 默认为 1Mbit/秒，TCP 默认无限制；
-t, --time #，以时间为测试结束条件进行测试，默认为 10 秒；
-n, --bytes #[KMG]，以数据传输大小为测试结束条件进行测试；
-k, --blockcount #[KMG]，以传输数据包数量为测试结束条件进行测试；
-l, --len #[KMG]，读写缓冲区的长度，TCP 默认为 128K，UDP 默认为 8K；
--cport ，指定 Client 端运行所使用的 TCP 或 UDP 端口，默认为临时端口；
-P, --parallel #，测试数据流并发数量；
-R, --reverse，反向模式运行（Server 端发送，Client 端接收）；
-w, --window #[KMG]，设置套接字缓冲区大小，TCP 模式下为窗口大小；
-C, --congestion ，设置 TCP 拥塞控制算法（仅支持 Linux 和 FreeBSD ）；
-M, --set-mss #，设置 TCP/SCTP 最大分段长度（MSS，MTU 减 40 字节）；
-N, --no-delay，设置 TCP/SCTP no delay，屏蔽 Nagle 算法；
-4, --version4，仅使用 IPv4；
-6, --version6，仅使用 IPv6；
-S, --tos N，设置 IP 服务类型（TOS，Type Of Service）；
-L, --flowlabel N，设置 IPv6 流标签（仅支持 Linux）；
-Z, --zerocopy，使用 “zero copy”（零拷贝）方法发送数据；
-O, --omit N，忽略前 n 秒的测试；
-T, --title str，设置每行测试结果的前缀；
--get-server-output，从 Server 端获取测试结果；
--udp-counters-64bit，在 UDP 测试包中使用 64 位计数器（防止计数器溢出）