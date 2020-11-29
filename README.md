# 1. Reproxy

用于给处于内网的服务器（无法连接外网）配置代理，将本地作为上网节点，使得服务器可以连接外网，从而配置环境更新依赖等等。

## 1.1. 使用背景

因为某种原因，手头有了一台服务器，而且是内网服务器，也就是说，只能通过 VPN 登录，而且，服务器无法连接因特网。

由于其性能很不错，所以设计了这样一个代理工具来设法让服务器连上外网。

## 1.2. 设计时序

**名词解释**：

- **Host**： 指的是可以连接互联网的那台主机。
- **Target**： 指的是无法连接外网的那台主机。

```mermaid
sequenceDiagram
    participant Internet
    participant Host port0
    participant Target port1
    participant Target port2
    participant APPs
    Host port0 -> Target port1: 请求建立 socket 连接
    Target port1 --> Host port0: 确认，建立 socket 连接
    loop Target
        APPs -> Target port2: port2 代理 target 上的所有流量
    end
    Target port2 -> Target port1: 程序内部数据转移
    Target port1 --> Host port0: 通过 socket 发送流量
    Host port0 -> Internet: 转发流量到Internet
    Internet --> Host port0: Host 收到 response
    Host port0 --> Target port1: Host 通过 socket 回复 Target
    Target port1 --> Target port2: 程序内部数据转移
    Target port2 --> APPs: 根据APP的端口进行回复
```
