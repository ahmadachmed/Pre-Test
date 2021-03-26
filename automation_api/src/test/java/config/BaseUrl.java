package config;

public class BaseUrl {
	  
	  String base = "https://jsonplaceholder.typicode.com";

	  public String urls(String slash) {
	    return base + slash;
	  }
	}