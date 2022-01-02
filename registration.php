public void login_click(object sender, EventArgs e)  
{  
    String username = TextBox1.Text.ToString();  
    String password = TextBox2.Text;  
    string con = ConfigurationManager.ConnectionStrings["DefaultConnection"].ToString();  
    SqlConnection connection = new SqlConnection(con);  
    connection.Open();  
ncrypt the given password  
    string passwords = encryption(password);  
    String query = "SELECT UserName, Password FROM UserAccount WHERE (UserName = '" + username + "') AND (Password = '"+passwords+"');";  
  
        SqlCommand cmd = new SqlCommand(query, connection);  
        SqlDataReader sqldr = cmd.ExecuteReader();  
        if (sqldr.Read())  
        {  
                Response.Redirect("Default3.aspx");  
        }  
            else  
            {  
                Label1.Text = "INVALID";   
                 
            }  
          
    connection.Close();  
}  