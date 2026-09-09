package com.example.firstapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class ThirdActivity extends AppCompatActivity {

    Button btn4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_third);

        btn4 = findViewById(R.id.back);

        btn4.setOnClickListener(view -> {

            Intent intent = new Intent(
                    ThirdActivity.this,
                    SecondActivity.class
            );

            startActivity(intent);
        });
    }
}