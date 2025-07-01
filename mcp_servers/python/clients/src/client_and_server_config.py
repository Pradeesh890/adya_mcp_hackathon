ClientsConfig =[
    "MCP_CLIENT_AZURE_AI",
    "MCP_CLIENT_OPENAI",
	"MCP_CLIENT_GEMINI"
]
ServersConfig = [
	{
		"server_name": "MYSQL",
		"command":"uv",
		"args": [
			"--directory",
			"D:/adya_mcp_hackathon/mcp_servers/python/servers/MYSQL/src/mysql_mcp_server",
			"run",
			"mysql_mcp_server"
		],
		"env": {
			"MYSQL_HOST": "localhost",
			"MYSQL_PORT": "3306",
			"MYSQL_USER": "test",
			"MYSQL_PASSWORD": "test123",
			"MYSQL_DATABASE": "my_db"
		}
	}
]