package com.example.semesterproject

import android.content.Context
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    private lateinit var temperatureTextView: TextView
    private lateinit var predictButton: Button
    private var weather = ""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        savedInstanceState?.let {
            loadWeatherFromBundle(it)
        } ?: run {
            loadWeatherFromSharedPrefs()
        }
        predictButton = findViewById(R.id.activity_main_predict_button)

        predictButton.setOnClickListener {
            displayRandomWeatherString()
        }
        temperatureTextView = findViewById(R.id.activity_main_weather_textView)
        temperatureTextView.setText(weather)
        temperatureTextView.setTextColor(getColor(R.color.red))
    }

    override fun onStop() {
        super.onStop()
        val sharedPrefs = getSharedPreferences(getString(R.string.preference_file_key), Context.MODE_PRIVATE)
        with(sharedPrefs.edit()) {
            putString(WEATHER_STATE, weather)
            apply()
        }
    }

    private fun displayRandomWeatherString() {
        var weatherArray = resources.getStringArray(R.array.weather_status_array)
        weather = weatherArray[Random.nextInt(weatherArray.size)]
        temperatureTextView.setText(weather)
    }

    private fun loadWeatherFromBundle(bundle: Bundle) {
        weather = bundle.getString(WEATHER_STATE).toString()
    }

    private fun loadWeatherFromSharedPrefs() {
        getSharedPreferences(
            getString(R.string.preference_file_key),
            Context.MODE_PRIVATE
        ).run {
            weather = getString(WEATHER_STATE, "" ).toString()
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.putString(WEATHER_STATE, weather)
        super.onSaveInstanceState(outState)
    }

    companion object {
        const val WEATHER_STATE  = "weather"
    }
}