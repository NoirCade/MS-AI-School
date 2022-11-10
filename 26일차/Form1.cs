using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;
using System.Collections;
using System.Runtime.InteropServices.WindowsRuntime;

namespace SQLServer1
{
    public partial class Form1 : Form
    {
        private const String CONNECTION_STRING = "Server=tcp:labuser36sqlserver.database.windows.net,1433;Initial Catalog=labuser36sql;Persist Security Info=False;User ID=labuser36;Password=@Seoul2022123;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
        private SqlConnection SqlCon = null;
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter();

        private DataSet dataMain = new DataSet();

        public Form1()
        {
            InitializeComponent();
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING); /*SQL DB와 연결*/
            btnConnect.Enabled = false; /*한번 연결 후 버튼을 사용할 수 없게 됨*/
        }

        private void btnGetData_Click(object sender, EventArgs e)
        {
            string query = "SELECT * FROM production.brands";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.CommandText = query;

            SqlApt.SelectCommand= cmd;
            SqlApt.Fill(dataMain); /*데이터를 dataMain에 넣어줘*/
            /*어댑터 객체를 이용하면 연결을 open, close하지 않아도 알아서 처리해준다!*/

            lstBrands.Items.Clear(); /*혹시 뭔가 있으면 일단 지운다*/

            DataRowCollection dataRows = dataMain.Tables[0].Rows;

            //Fill to DataGridView - DataGridView 창에 목록 생성
            for (int i = 0; i < dataRows.Count; i++)
            {
                lstBrands.Items.Add(dataRows[i][1].ToString());
            }
            
            btnGetData.Enabled = false;
        }

        private void lstBrands_SelectedIndexChanged(object sender, EventArgs e)
        {
            /*원하는 목차대로 데이터를 표시하려면, 1. 한번에 전체 데이터를 불러와서 클릭하면 잘라서 보여주거나, 2. 그때그때 필요한 만큼씩 불러온다.
            1번 방법은 쿼리 1번에 끝나므로 데이터 베이스 부담이 줄어드나, 조금 더 복잡하니 우선 2번 방법을 사용!*/
            if(lstBrands.SelectedIndex == -1)
            {
                return;
            }

            int selectedIndex = lstBrands.SelectedIndex;
            int selectedBrandID = Int32.Parse(dataMain.Tables[0].Rows[selectedIndex][0].ToString());
            /*Int32.Parse를 이용해서 정수로 전환하는데, 해당 메소드는 문자열만 정수로 전환하므로 먼저 문자열로 전환...*/   
            
            DataSet dataProducts = new DataSet();
            String query = "SELECT * FROM production.products WHERE brand_id = @brand_id";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.Parameters.Add(new SqlParameter("@brand_id", SqlDbType.Int)).Value = selectedBrandID;
            cmd.CommandText = query;
            
            SqlApt.SelectCommand= cmd;
            SqlApt.Fill(dataProducts);
            grdProducts.DataSource = dataProducts.Tables[0];
        }

        private void btnVIPMembers_Click(object sender, EventArgs e)
        {
            frmVIPMembers vip = new frmVIPMembers();
            vip.ShowDialog();
            /*새로운 폼을 띄우는 것은 Show와 ShowDialog 두가지 메소드가 있는데, ShowDialog의 경우, 새로 열린 폼에서 작업을 마칠 때까지
            기존 폼에서 작업할 수 없다!*/
        }
    }
}
