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

namespace SQLServer1
{
    public partial class frmVIPMembers : Form
    {
        private const String CONNECTION_STRING = "Server=tcp:labuser36sqlserver.database.windows.net,1433;Initial Catalog=labuser36sql;Persist Security Info=False;User ID=labuser36;Password=@Seoul2022123;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
        private SqlConnection SqlCon = null;
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter();
        private DataSet dataMain = new DataSet();
        public frmVIPMembers()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void frmVIPMembers_Load(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING); /*SQL DB와 연결*/

            string query = "SELECT * FROM dbo.VIPmembers";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.CommandText = query;

            SqlApt.SelectCommand = cmd;
            SqlApt.Fill(dataMain); /*데이터를 dataMain에 넣어줘*/

            grdMemberList.DataSource = dataMain.Tables[0];
        }
    }
}
