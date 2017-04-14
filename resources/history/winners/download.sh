function download() {
  rm -rf $1 2> /dev/null
  mkdir $1

  cd $1
  for year in $(seq $2 $3) ; do
    wget $4$year.htm -O $year.htm
  done
  cd ..
}

download big_lottery_649 2004 2017 http://www.nfd.com.tw/lotto/b
download taiwan_lottery_638 2002 2008 http://www.nfd.com.tw/lotto/m
download power_lottery_638 2008 2017 http://www.nfd.com.tw/lotto/p-
# download today_lottery_539 2007 2017 
download dafu_lottery_740 2015 2017 http://www.nfd.com.tw/lotto/40-
# download 4_d_lottery 2003 2017 
