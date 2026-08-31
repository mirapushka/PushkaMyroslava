using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace АОП_4пр
{
    public partial class Form1 : Form
    {
        List<Point> centers = new List<Point>();
        List<int> sizes = new List<int>();
        List<int> types = new List<int>();
        List<Color> fillColors = new List<Color>();
        List<Color> lineColors = new List<Color>();
        Color colorFill = Color.Yellow;
        Color colorLine = Color.Black;

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.Items.Clear();
            comboBox1.Items.AddRange(new string[] { "Тип 1 (5 пр.)", "Тип 2 (6 пр.)", "Тип 3 (8 пр.)" });
            comboBox1.SelectedIndex = 0;
            numericUpDown1.Minimum = 10;
            numericUpDown1.Maximum = 500;
            numericUpDown1.Value = 50;
        }
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            for (int i = 0; i < centers.Count; i++)
            {
                int x = centers[i].X;
                int y = centers[i].Y;
                int r = sizes[i];
                int rays = types[i];
                PointF[] pts = new PointF[rays * 2];
                double startAngle = -Math.PI / 2;
                double step = Math.PI / rays;

                for (int j = 0; j < rays * 2; j++)
                {
                    double curR = (j % 2 == 0) ? r : r / 2.5;
                    pts[j] = new PointF(
                        (float)(x + curR * Math.Cos(startAngle + j * step)),
                        (float)(y + curR * Math.Sin(startAngle + j * step))
                    );
                }
                using (SolidBrush br = new SolidBrush(fillColors[i]))
                using (Pen pn = new Pen(lineColors[i], 2))
                {
                    e.Graphics.FillPolygon(br, pts);
                    e.Graphics.DrawPolygon(pn, pts);
                }
            }
        }
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            centers.Add(e.Location);
            sizes.Add((int)numericUpDown1.Value);
            int rays = 5;
            if (comboBox1.SelectedIndex == 1) rays = 6;
            if (comboBox1.SelectedIndex == 2) rays = 8;
            types.Add(rays);
            fillColors.Add(colorFill);
            lineColors.Add(colorLine);
            listBox1.Items.Add($"Зірка {rays} пр. [{e.X}, {e.Y}]");
            pictureBox1.Invalidate();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            ColorDialog cd = new ColorDialog();
            if (cd.ShowDialog() == DialogResult.OK)
            {
                colorFill = cd.Color;
                button1.BackColor = cd.Color; 
            }
        }
        private void button2_Click(object sender, EventArgs e)
        {
            ColorDialog cd = new ColorDialog();
            if (cd.ShowDialog() == DialogResult.OK)
            {
                colorLine = cd.Color;
                button2.ForeColor = cd.Color;
            }
        }
        private void button3_Click(object sender, EventArgs e)
        {
            int idx = listBox1.SelectedIndex;
            if (idx != -1)
            {
                centers.RemoveAt(idx);
                sizes.RemoveAt(idx);
                types.RemoveAt(idx);
                fillColors.RemoveAt(idx);
                lineColors.RemoveAt(idx);
                listBox1.Items.RemoveAt(idx);

                pictureBox1.Invalidate(); 
            }
        }
        private void button4_Click(object sender, EventArgs e)
        {
            centers.Clear();
            sizes.Clear();
            types.Clear();
            fillColors.Clear();
            lineColors.Clear();
            listBox1.Items.Clear();

            pictureBox1.Invalidate(); 
        }
        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
        }
    }
}