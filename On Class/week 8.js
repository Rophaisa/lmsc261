function getRange(midiNote)
{
    if (midiNote >= 0 && midiNote < 32)
    {
        return "bass";
    } else if (midiNote >=32 && midiNote <64)
    {
        return;
    } else if (midiNote >=64 && midiNote < 96)
    {
        print("you're an alto");
    } else if (midiNote >=96 && midiNote < 127) {
        print("you're a diva");
    } else {
        print("you're weird");
    }
}


let range = getRange(300)
print("The musixian is: " + range)