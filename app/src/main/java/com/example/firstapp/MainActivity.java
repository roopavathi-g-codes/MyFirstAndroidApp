package com.example.firstapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        btn = findViewById(R.id.button);

        btn.setOnClickListener(view -> {

            Intent intent = new Intent(
                    MainActivity.this,
                    SecondActivity.class
            );

            startActivity(intent);

            Toast.makeText(
                    MainActivity.this,
                    "login successfully.",
                    Toast.LENGTH_LONG
            ).show();
        });
    }
}