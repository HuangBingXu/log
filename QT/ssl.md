### 环境
QT5对OpenSSL的编程实现了支持，但是却没有附带对应的二进制运行库，这就会使得你的程序代码编译是正确通过的，但是在IDE里头运行调试时，会报SSL错误：
```
QSslSocket: cannot call unresolved function SSLv23_client_method
QSslSocket: cannot call unresolved function SSL_CTX_new
QSslSocket: cannot call unresolved function SSL_library_init
QSslSocket: cannot call unresolved function ERR_get_error
QSslSocket: cannot call unresolved function ERR_get_error
```
解决的方法是复制OpenSSL的运行库到QT中，对于windows版本来说是这两个dll链接库：

    ssleay32.dll
    libeay32.dll

这两个文件可以从**Qt\Qt5.12.0\Tools\mingw730_64\opt\bin**拷贝到**Qt\Qt5.12.0\Tools\mingw730_64**

###### [参考](http://www.mr-wu.cn/using-self-signed-certificates-request-rest-api-in-qt-code/)

### 测试
```
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QNetworkAccessManager *manager = new QNetworkAccessManager(this);
    QUrl url("https://www.devbean.net/2013/10/qt-study-road-2-access-network-1/");
    QNetworkRequest request(url);

    QSslConfiguration config;

    config.setPeerVerifyMode(QSslSocket::VerifyNone);
    config.setProtocol(QSsl::TlsV1_0);
    request.setSslConfiguration(config);
    connect(manager, SIGNAL(finished(QNetworkReply*)), this, SLOT(replyFinished(QNetworkReply*)));
    manager->get(request);
}

void MainWindow::replyFinished(QNetworkReply *reply)  //当回复结束后
{
    QByteArray all = reply->readAll();
    qDebug()<<"len:"<<all.length();
}
```