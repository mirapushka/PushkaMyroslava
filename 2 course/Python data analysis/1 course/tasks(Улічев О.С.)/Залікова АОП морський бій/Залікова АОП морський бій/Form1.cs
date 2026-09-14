using System.DirectoryServices;
using System;
using System.Drawing;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Залікова_АОП_морський_бій
{
    public partial class Form1 : Form
    {

        private void Form1_Load(object sender, EventArgs e)
        { }
        public const int mapSize = 10;
        public int cellSize = 30;
        public string alphabet = "АБВГДЕЖЗИК";

        public int[,] myMap = new int[mapSize, mapSize];
        public int[,] enemyMap = new int[mapSize, mapSize];

        public Button[,] myButtons = new Button[mapSize, mapSize];
        public Button[,] enemyButtons = new Button[mapSize, mapSize];

        public bool isPlaying = false;

        public Bot bot;


        public Form1()
        {
            InitializeComponent();
            this.Text = "Морський бій";

            Init();
        }
        public void Init()
        {
            isPlaying = false;
            CreateMap();
            bot = new Bot(enemyMap, myMap, enemyButtons, myButtons);
            enemyMap = bot.ConfigureShips();
        }
        public void CreateMap()
        {
            this.Width = mapSize * 2 * cellSize + 80;
            this.Height = (mapSize + 5) * cellSize + 20;
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    myMap[i, j] = 0;
                    Button button = new Button();
                    button.Location = new Point(j * cellSize, i * cellSize);
                    button.Size = new Size(cellSize, cellSize);
                    button.Click += new EventHandler(ConfigureShips);
                    button.BackColor = Color.White;
                    if (j == 0 || i == 0)
                    {
                        button.BackColor = Color.Gray;
                        if (i == 0 && j > 0)
                            button.Text = alphabet[j - 1].ToString();
                        if (j == 0 && i > 0)
                            button.Text = i.ToString();
                    }
                    myButtons[i,j] = button;
                    this.Controls.Add(button);

                }
            }
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    myMap[i, j] = 0;
                    enemyMap[i, j] = 0;
                    Button button = new Button();
                    button.Location = new Point(350 + j * cellSize, i * cellSize);
                    button.Size = new Size(cellSize, cellSize);
                    if (j == 0 || i == 0)
                    {
                        button.BackColor = Color.Gray;
                        if (i == 0 && j > 0)
                            button.Text = alphabet[j - 1].ToString();
                        if (j == 0 && i > 0)
                            button.Text = i.ToString();
                    }
                    else
                    {
                        button.Click += new EventHandler(PlayerShoot);
                    }
                    this.Controls.Add(button);
                    enemyButtons[i, j] = button;
                }
            }
            Label map1 = new Label();
            map1.Text = "Карта гравця";
            map1.AutoSize = true;
            map1.Location = new Point(110, mapSize * cellSize + 10);
            map1.TextAlign = ContentAlignment.MiddleCenter;
            this.Controls.Add(map1);

            Label map2 = new Label();
            map2.Text = "Карта ворога";
            map2.AutoSize = true;
            map2.Location = new Point(350 + 110, mapSize * cellSize + 10);
            map2.TextAlign = ContentAlignment.MiddleCenter;
            this.Controls.Add(map2);

            Button startButton = new Button();
            startButton.Text = "Почати";
            startButton.Click += new EventHandler(Start);
            startButton.AutoSize = true;
            startButton.Location = new Point(300, mapSize * cellSize + 30);
            this.Controls.Add(startButton);

        }
        public void Start(object sender, EventArgs e)
        {
        isPlaying = true;
            }
        public bool CheckIfMapIsNotEmpty()
        {
            bool IsEmpty1 = true;
            bool IsEmpty2 = true;
            for (int i = 1; i <  mapSize; i++)
            {
                for (int j = 1; j < mapSize; j++)
                {
                    if (myMap[i, j] != 0)
                        IsEmpty1 = false;
                    if (enemyMap[i, j] != 0)
                        IsEmpty2 = false;
                }
            }
            if (IsEmpty1 || IsEmpty2)
                return false;
            else return true;
        }
        public void ConfigureShips(object sender, EventArgs e)
        {
            Button pressedButton = sender as Button;
            if (pressedButton.BackColor == Color.Gray)
            {
                return; 
            }
            if (isPlaying)
            {
                if (myMap[pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize] == 0)
                {
                    pressedButton.BackColor = Color.Red;
                    myMap[pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize] = 1;
                }
                else
                {
                    pressedButton.BackColor = Color.White;
                    myMap[pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize] = 0;
                }

            }
        }
        public async void PlayerShoot(object sender, EventArgs e)
        {

            Button pressedButton = sender as Button;
            if (pressedButton.BackColor == Color.Blue || pressedButton.BackColor == Color.Black)
                return;
            bool playerTurn = Shoot(enemyMap, pressedButton);
            if (!playerTurn && isPlaying)
            {
                bool botHit = true;
                while (botHit && isPlaying)
                {
                    await Task.Delay(800);
                    botHit = bot.Shoot();
                    if (!CheckIfMapIsNotEmpty())
                    {
                        isPlaying = false;
                        MessageBox.Show("Гра закінчена!");
                        this.Controls.Clear();
                        Init();
                    }


                }
            }
        }
        public bool Shoot(int[,] map, Button pressedButton)
        {
            bool hit = false;
            if(isPlaying)
            {
                int delta = 0;
                if (pressedButton.Location.X > 300)
                    delta = 350;
                int y = pressedButton.Location.Y / cellSize;
                int x = (pressedButton.Location.X - delta) / cellSize;
                if (map[y, x] != 0)
                {
                    hit = true;
                    map[pressedButton.Location.Y / cellSize, (pressedButton.Location.X - delta) / cellSize] = 0;
                    pressedButton.BackColor = Color.Blue;
                    pressedButton.Text = "X";

                }
                else
                {
                    hit = false;
                    pressedButton.BackColor = Color.Black;
                }
            }
            return hit;

        }
    }
       
}
