    QDateTime dt;
    QString current_dt = dt.currentDateTime().toString("yyyy:MM:dd:hh:mm:ss:zzz");
    qsrand(dt.currentDateTime().toTime_t());
    QString rand = qrand();