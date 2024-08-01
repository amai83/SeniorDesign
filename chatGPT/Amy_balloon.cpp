#include <iostream>

using namespace std;

class Balloon
{
protected:
    static float PointsPerBalloon;
    static float PointsMultiplier;
    static float PointsTotal;
    static int BalloonCount;

public:
    Balloon();
    virtual ~Balloon() = 0;
    static int GetBalloonCount();
    static float GetPointTotal();
    virtual char GetIdentifier() const;
};

class RedBalloon : public Balloon
{
public:
    virtual char GetIdentifier() const;
    ~RedBalloon();
};

class BlueBalloon : public Balloon
{
public:
    virtual char GetIdentifier() const;
    ~BlueBalloon();
};

class YellowBalloon : public Balloon
{
public:
    virtual char GetIdentifier() const;
    ~YellowBalloon();
};

// Init static variables.
float Balloon::PointsPerBalloon = 1.0;
float Balloon::PointsMultiplier = 1.0;
float Balloon::PointsTotal = 1.0;
int Balloon::BalloonCount = 0;

Balloon::Balloon()
{
    BalloonCount++;
}
Balloon::~Balloon()
{
    BalloonCount--;
    PointsTotal = PointsPerBalloon * PointsMultiplier;
}
int Balloon::GetBalloonCount()
{
    return BalloonCount;
}
float Balloon::GetPointTotal()
{
    return PointsTotal;
}
char Balloon::GetIdentifier() const
{
    return '\0';
}

char RedBalloon::GetIdentifier() const
{
    return 'R';
}
RedBalloon::~RedBalloon()
{
    PointsMultiplier = PointsMultiplier + 0.1;
    cout << " Red Balloon - *POP* " << endl;
}

char BlueBalloon::GetIdentifier() const
{
    return 'B';
}

BlueBalloon::~BlueBalloon()
{
    PointsPerBalloon = PointsPerBalloon + 0.1;
    cout << " Blue Balloon - *POP* " << endl;
}

char YellowBalloon::GetIdentifier() const
{
    return 'Y';
}
YellowBalloon::~YellowBalloon()
{
    cout << " Yellow Balloon - *POP* " << endl;
}