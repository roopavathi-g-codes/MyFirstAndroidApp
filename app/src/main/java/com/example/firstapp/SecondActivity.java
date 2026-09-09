package com.example.firstapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class SecondActivity extends AppCompatActivity {

    Button btn2, btn3, btn4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_second);

        // NEXT BUTTON
        btn2 = findViewById(R.id.next);

        btn2.setOnClickListener(view -> {

            Intent intent = new Intent(
                    SecondActivity.this,
                    ThirdActivity.class
            );

            startActivity(intent);
        });


        // BACK BUTTON
        btn3 = findViewById(R.id.back);

        btn3.setOnClickListener(view -> {

            Intent intent = new Intent(
                    SecondActivity.this,
                    MainActivity.class
            );

            startActivity(intent);
        });


        // WEBSITE BUTTON
        btn4 = findViewById(R.id.button4);

        btn4.setOnClickListener(view -> {

            Intent webIntent = new Intent(
                    Intent.ACTION_VIEW,
                    Uri.parse("https://www.viswamgroup.com")
            );

            startActivity(webIntent);
        });
    }
}