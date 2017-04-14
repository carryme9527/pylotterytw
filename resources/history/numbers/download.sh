function download() {
  rm -rf $1 2> /dev/null
  mkdir $1

  cd $1
  for year in $(seq $2 $3) ; do
    if [ "$5" = true ] ; then
      wget $4f$year.htm -O $year.htm # additional `f` between $4 & $year
    else
      wget $4$year.htm -O $year.htm # $4 attached by $year
    fi
  done
  cd ..
}

download big_lottery_649 2004 2017 http://www.nfd.com.tw/lottery/49-year/49- true
download taiwan_lottery_638 2002 2008 http://www.nfd.com.tw/lottery/lottyear/ true
download power_lottery_638 2008 2017 http://www.nfd.com.tw/lottery/power-38/ true
download today_lottery_539 2007 2017 http://www.nfd.com.tw/lottery/39-year/39- true
download dafu_lottery_740 2015 2017 http://www.nfd.com.tw/lottery/40-year/40- true
download 4_d_lottery 2003 2017 http://www.nfd.com.tw/lottery/4-star/ false
