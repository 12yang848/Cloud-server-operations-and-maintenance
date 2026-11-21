云端实战项目

本项目基于阿里云 ECS (Ubuntu 22.04)，完成了个人全栈站点的从零部署与运维闭环。

技术栈
- **系统与网络**：Ubuntu, TCP/IP, DNS, 防火墙安全组配置
- **容器化编排**：Docker, Docker Compose
- **Web 服务**：Nginx (反向代理, SSL 证书, HTTP 301 强制跳转)
- **数据库**：MySQL 8.0 (数据卷持久化)
- **自动化**：Python (psutil, smtplib), Crontab 定时巡检

项目亮点
- 独立配置并上线 HTTPS 全站加密。
- 解决宿主机端口冲突、Nginx 证书路径丢失、YAML 缩进错误等真实生产故障。
- 基于 Python 实现服务器资源监控与邮件告警。

🔗 [点击访问我的个人主页](https://yllzero.xyz)
