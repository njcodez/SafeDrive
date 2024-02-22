package com.example.lasagna

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.lasagna.databinding.ActivityLoginPageBinding
import com.example.lasagna.databinding.ActivitySignupPageBinding

class SignupPage : AppCompatActivity() {

    private lateinit var binding: ActivitySignupPageBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding : ActivitySignupPageBinding = ActivitySignupPageBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnsignup2.setOnClickListener {
            val intent = Intent(this, Home::class.java)
            startActivity(intent)
        }
    }
}