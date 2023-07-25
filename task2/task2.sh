
kishkindha_id=553
madra_id=828
usinara_id=723
heheya_id=698


total_count=0

count_people() {
    local id=$1
    local count=$(grep -c "$id" users.txt)
    echo "$count"
}

kishkindha_count=$(count_people "$kishkindha_id")
madra_count=$(count_people "$madra_id")
usinara_count=$(count_people "$usinara_id")
heheya_count=$(count_people "$heheya_id")


total_count=$((kishkindha_count + madra_count + usinara_count + heheya_count))


echo "Total number of people: $total_count"
