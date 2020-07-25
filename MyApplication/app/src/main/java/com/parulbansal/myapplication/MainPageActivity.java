package com.parulbansal.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.Configuration;
import android.content.res.Resources;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainPageActivity extends AppCompatActivity {
    Locale myLocale;
    SharedPreferences sh;
    SharedPreferences.Editor editor ;
    //    private String mResendToken;
    public void setLocale(String lang) {

        myLocale = new Locale(lang);
        Resources res = getResources();
        DisplayMetrics dm = res.getDisplayMetrics();
        Configuration conf = res.getConfiguration();
        conf.locale = myLocale;
        res.updateConfiguration(conf, dm);

        Intent refresh = new Intent(this, MainActivity.class);
        startActivity(refresh);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_page);
        Spinner spinner = (Spinner) findViewById(R.id.spinner1);
        sh= getApplicationContext().getSharedPreferences("MyPref", 0);
         editor=sh.edit();
       
         if(sh.getString("locale","")=="") {
             editor.putString("locale", "en");
             editor.commit();
         }
         else
         {
             if(sh.getString("locale","") == "en")
             {
                 spinner.setSelection(0);
             }
             else if(sh.getString("locale","")=="ta")
             {
                 spinner.setSelection(1);
             }
         }
        // Spinner click listener
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String item = adapterView.getItemAtPosition(i).toString();

                  Log.d("locale",sh.getString("locale","").toString());

                if(sh.getString("locale","en") != "en" && i==0) {

                        Toast.makeText(adapterView.getContext(),
                                "You have selected English", Toast.LENGTH_SHORT).show();
                        editor.putString("locale","en");
                        editor.commit();
                        setLocale("en");

                    }
                else if(sh.getString("locale","en") != "ta" && i==1 ){
                        Toast.makeText(adapterView.getContext(),
                                "You have selected Tamil", Toast.LENGTH_SHORT).show();
                        editor.putString("locale","ta");
                        editor.commit();
                        setLocale("ta");

                    }



            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        // Spinner Drop down elements
        List<String> categories = new ArrayList<String>();
        categories.add("English");
        categories.add("Tamil");


        // Creating adapter for spinner
        ArrayAdapter<String> dataAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, categories);

        // Drop down layout style - list view with radio button
        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        // attaching data adapter to spinner
        spinner.setAdapter(dataAdapter);


    }
}