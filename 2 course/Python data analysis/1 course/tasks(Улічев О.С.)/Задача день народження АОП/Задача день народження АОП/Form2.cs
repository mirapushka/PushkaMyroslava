using System;
using System.Windows.Forms;

namespace Задача_день_народження_АОП
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }
        private void label1_Click(object sender, EventArgs e)
        {
        }
        private void button1_Click(object sender, EventArgs e)
        {
            string name = textBox1.Text;
            if (string.IsNullOrWhiteSpace(name))
            {
                MessageBox.Show("Будь ласка, введіть ім'я!");
                return;
            }

            DateTime birthDate = dateTimePicker1.Value;
            DateTime today = DateTime.Today;
            DateTime nextBirthday = new DateTime(today.Year, birthDate.Month, birthDate.Day);

            if (nextBirthday < today)
            {
                nextBirthday = nextBirthday.AddYears(1);
            }
            int daysLeft = (nextBirthday - today).Days;

            if (daysLeft == 0)
            {
                MessageBox.Show($"Вітаю, {name}! Ваш день народження сьогодні!");
            }
            else
            {
                MessageBox.Show($"Вітаю, {name}! До дня народження залишилося днів: {daysLeft}");
            }
            this.Close();
        }
    }
}