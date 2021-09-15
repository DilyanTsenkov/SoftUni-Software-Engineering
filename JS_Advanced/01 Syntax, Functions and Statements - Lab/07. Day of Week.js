function dayOfWeek(day) {
    let result
    if (day == 'Monday') {
        result = 1;
    }
    if (day == 'Tuesday') {
        result = 2;
    }
    if (day == 'Wednesday') {
        result = 3;
    }
    if (day == 'Thursday') {
        result = 4;
    }
    if (day == 'Friday') {
        result = 5;
    }
    if (day == 'Saturday') {
        result = 6;
    }
    if (day == 'Sunday') {
        result = 7;
    }
    if (result) {
        console.log(result);
    } else {
        console.log('error');
    }
}

dayOfWeek('Monday');
dayOfWeek('Tuesday');
dayOfWeek('Invalid');
dayOfWeek('Wednesday');
dayOfWeek('Thursday');
dayOfWeek('Invalid');
dayOfWeek('Friday');
dayOfWeek('Invalid');
dayOfWeek('Saturday');
dayOfWeek('Sunday');
dayOfWeek('Invalid');