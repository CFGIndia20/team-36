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
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainPageActivity extends AppCompatActivity {
    Locale myLocale;
    SharedPreferences sh;
    SharedPreferences.Editor editor ;
    private FirebaseDatabase database=FirebaseDatabase.getInstance();
    DatabaseReference reference;
    Member member;
    int i=0;
    RadioButton r1,r2,r3,r4;
    String f1=":(",f2=":)",f3=":D";
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

         if(sh.getString("locale","").equals("")) {
             editor.putString("locale", "en");
             editor.commit();
         }
         else
         {
             if(sh.getString("locale","").equals("en"))
             {
                 spinner.setSelection(0);
             }
             else if(sh.getString("locale","").equals("ta"))
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

                if(!sh.getString("locale","en").equals("en")  && i==0) {

                        Toast.makeText(adapterView.getContext(),
                                "You have selected English", Toast.LENGTH_SHORT).show();
                        editor.putString("locale","en");
                        editor.commit();
                        setLocale("en");

                    }
                else if(!sh.getString("locale","en").equals("ta") && i==1 ){
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
        reference=database.getInstance().getReference().child("feedback");
        member=new Member();
        Button submit=findViewById(R.id.button_confirm_next);
        r1=findViewById(R.id.radio_button1);
        r2=findViewById(R.id.radio_button2);
        r3=findViewById(R.id.radio_button3);

        reference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if(snapshot.exists())
                {
                    i=(int)snapshot.getChildrenCount();
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
             if(r1.isChecked())
             {
               member.setFeedback(f1);
               reference.child(String.valueOf(i+1)).setValue(member);
             }
             else if (r2.isChecked())
             {
                 member.setFeedback(f2);
                 reference.child(String.valueOf(i+1)).setValue(member);
             }
             else if(r3.isChecked())
             {
                 member.setFeedback(f3);
                 reference.child(String.valueOf(i+1)).setValue(member);
             }
            }
        });
        Button mLogout=findViewById(R.id.logout);
        mLogout.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view) {
                FirebaseAuth.getInstance().signOut();
                Intent intent = new Intent(getApplicationContext(),MainActivity.class);
                intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                startActivity(intent);
                finish();
                return;
            }
        });

    }
}