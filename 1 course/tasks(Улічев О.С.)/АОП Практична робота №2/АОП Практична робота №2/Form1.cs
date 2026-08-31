using System;
using System.Collections.Generic;
using System.Windows.Forms;
namespace АОП_Практична_робота__2
{
    public partial class Form1 : Form
    {
        class Unit { public string Name; public double Ratio; }
        class Category { public string Name; public List<Unit> Units = new List<Unit>(); }
        List<Category> allData = new List<Category>();
        public Form1()
        {
            InitializeComponent();
            InitMyData();
        }
        private void InitMyData()
        {
            var distance = new Category { Name = "Відстань" };
            distance.Units.Add(new Unit { Name = "Метр", Ratio = 1.0 });
            distance.Units.Add(new Unit { Name = "Кілометр", Ratio = 1000.0 });
            distance.Units.Add(new Unit { Name = "Сантиметр", Ratio = 0.01 });
            distance.Units.Add(new Unit { Name = "Міліметр", Ratio = 0.001 });
            distance.Units.Add(new Unit { Name = "Миля", Ratio = 1609.34 });
            allData.Add(distance);
            var weight = new Category { Name = "Вага" };
            weight.Units.Add(new Unit { Name = "Грам", Ratio = 1.0 });
            weight.Units.Add(new Unit { Name = "Кілограм", Ratio = 1000.0 });
            weight.Units.Add(new Unit { Name = "Тонна", Ratio = 1000000.0 });
            weight.Units.Add(new Unit { Name = "Фунт", Ratio = 453.59 });
            weight.Units.Add(new Unit { Name = "Унція", Ratio = 28.35 });
            allData.Add(weight);
            comboBox1.Items.Clear();
            foreach (var cat in allData)
            {
                comboBox1.Items.Add(cat.Name);
            }
            if (comboBox1.Items.Count > 0)
            {
                comboBox1.SelectedIndex = 0;
            }
        }
        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            int index = comboBox1.SelectedIndex;
            if (index == -1) return;
            comboBox2.Items.Clear();
            comboBox3.Items.Clear();
            foreach (var unit in allData[index].Units)
            {
                comboBox2.Items.Add(unit.Name);
                comboBox3.Items.Add(unit.Name);
            }
            if (comboBox2.Items.Count > 0)
            {
                comboBox2.SelectedIndex = 0;
                comboBox3.SelectedIndex = 1;
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            string inputText = textBox1.Text.Replace('.', ',');

            if (double.TryParse(inputText, out double inputVal))
            {
                int catIdx = comboBox1.SelectedIndex;
                int fromIdx = comboBox2.SelectedIndex;
                int toIdx = comboBox3.SelectedIndex;
                if (catIdx == -1 || fromIdx == -1 || toIdx == -1) return;
                double fromRatio = allData[catIdx].Units[fromIdx].Ratio;
                double toRatio = allData[catIdx].Units[toIdx].Ratio;
                double result = (inputVal * fromRatio) / toRatio;
                textBox2.Text = result.ToString("G10");
            }
            else
            {
                MessageBox.Show("Введіть число!");
            }
        }
    }
}
