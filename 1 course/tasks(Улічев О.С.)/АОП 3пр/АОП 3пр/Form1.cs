namespace АОП_3пр
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Pen bluePen = new Pen(Color.Blue, 2);
            Pen blackPen = new Pen(Color.Black, 5);
            Pen redPen = new Pen(Color.Red, 3);
            Pen woodPen = new Pen(Color.Brown, 4);
            g.DrawEllipse(bluePen, 150, 200, 100, 100);
            g.DrawEllipse(bluePen, 160, 130, 80, 80);
            g.DrawEllipse(bluePen, 170, 70, 60, 60);
            g.DrawLine(woodPen, 160, 170, 100, 150);
            g.DrawLine(woodPen, 240, 170, 300, 150);
            Point[] nose = {
                new Point(200, 100),
                new Point(200, 110),
                new Point(240, 105)
            };
            g.DrawPolygon(redPen, nose);
            g.DrawArc(blackPen, 185, 100, 30, 20, 0, 180);
            g.DrawRectangle(blackPen, 175, 40, 50, 35);
            bluePen.Dispose();
            blackPen.Dispose();
            redPen.Dispose();
            woodPen.Dispose();
        }
    }
}