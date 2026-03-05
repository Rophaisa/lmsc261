function pickRandomActivity() {
const dailyActivities = [
        "Clean Solar Panel",
        "Video Chat with Houston",
        "Hydrate Space Food",
        "Take Earth Picture",
        "Learn Russian",
        "Learn LMSC!!!!"
    ];

    let randomIndex = Math.random() * dailyActivities.length;
    let randomActivity = Math.floor(randomIndex);


    return dailyActivities[randomActivity];
}

print ("Today's activity is: " + pickRandomActivity());